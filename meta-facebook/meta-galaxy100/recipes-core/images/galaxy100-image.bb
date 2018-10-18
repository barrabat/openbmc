# Copyright 2018-present Facebook. All Rights Reserved.

inherit aspeed_uboot_image

require recipes-core/images/fb-openbmc-image.bb

# Changing the image compression from gz to lzma achieves 30% saving (~3M).
IMAGE_FSTYPES += "cpio.lzma.u-boot"

# Include modules in rootfs
IMAGE_INSTALL += " \
  packagegroup-openbmc-base \
  packagegroup-openbmc-net \
  packagegroup-openbmc-python3 \
  packagegroup-openbmc-rest3 \
  at93cx6-util \
  bcm5396-util \
  bitbang \
  cpldupdate \
  flashrom \
  ipmid \
  lldp-util \
  mterm \
  memtester  \
  mkeeprom  \
  openbmc-utils \
  openbmc-gpio \
  po-eeprom \
  repeater  \
  retimer  \
  kcsd \
  spatula \
  stress  \
  usb-console \
  wedge-eeprom \
  watchdogd \
  "

IMAGE_FEATURES += " \
  ssh-server-openssh \
  tools-debug \
  "

DISTRO_FEATURES += " \
  ext2 \
  ipv6 \
  nfs \
  usbgadget \
  usbhost \
  "
