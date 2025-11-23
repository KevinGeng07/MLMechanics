Generate Adversarial Network

GANs generate images using two networks playing adversairal games against each other. The Generator produces adversarial data to obfuscate correct model training, while the Discriminator classifies data as either real or fake (generated, adversarial). In training, both models follow an equivalent, yet independent pipeline, resulting in two losses & two optimizers. As the Generator beings producing more accurate data, the Discriminator has a more difficult time distinguishing between real & generated data.

Paper: (Generative Adversarial Networks)[https://arxiv.org/pdf/1406.2661]