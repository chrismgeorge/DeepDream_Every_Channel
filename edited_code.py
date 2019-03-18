torch.save(netG, '%s/netG_model_%d.pth' % (outf, epoch))

PATH = '%s/netG_model_%d.pth' % (outf, epoch)
netG = torch.load(PATH)

def interpolate(A, B, num_interps):
  if A.shape != B.shape:
    raise ValueError('A and B must have the same shape to interpolate.')
  alphas = np.linspace(0, 1, num_interps)
  return np.array([(1-a)*A + a*B for a in alphas])

mu, sigma = 0., 1.
list_of_images = []
arr1 = np.random.lognormal(mu, sigma, [1, 100, 1, 1])
for i in range(20):
    arr2 = np.random.lognormal(mu, sigma, [1, 100, 1, 1])

    numOfInterps = random.randint(12)
    interps = interpolate(arr1, arr2, numOfInterps)

    for ee in range(numOfInterps):
        arr = interps[ee]
        noise1 = torch.FloatTensor(arr)
        noise1 = noise1.cuda()
        noisev = Variable(noise1)
        fake = netG(noisev)
        fake=fake.cpu()
        list_of_images.append(make_grid(fake.data, padding=0).numpy().tolist())

    arr1 = arr2

p_array_of_processed_images = np.asarray(list_of_images, dtype=float)
np.save('./numpy_images.npy', p_array_of_processed_images)
