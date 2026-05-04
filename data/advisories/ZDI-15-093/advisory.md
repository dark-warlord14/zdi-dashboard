# ZDI-15-093: (Mobile Pwn2Own) Google Android DHCP Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-093
- **ZDI-CAN:** ZDI-CAN-2620
- **Date:** 2015-03-12
- **CVE:** CVE-2014-7912
- **CVSS:** 5.1
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Google
- **Affected Products:** Android
- **Credit:** Jüri Aedla
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-093/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Google Android. Authentication is not required to exploit this vulnerability. The specific flaw exists within the parsing of the DHCP options in a DHCP ACK packet. The vulnerability is triggered when the LENGTH of an option, when added to the current read position, exceeds the actual length of the DHCP options buffer. An attacker can leverage this vulnerability to execute code on the device.

## Additional Details

Google has issued an update to correct this vulnerability. More details can be found at: https://android.googlesource.com/platform/external/dhcpcd/+/73c09dd8067250734511d955d8f792b41c7213f0

## Disclosure Timeline

- 2014-11-13 - Vulnerability reported to vendor
- 2015-03-12 - Coordinated public release of advisory
