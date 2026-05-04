# ZDI-15-160: (Mobile Pwn2Own) Amazon App Store HTTPS Downgrade Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-160
- **ZDI-CAN:** ZDI-CAN-2618
- **Date:** 2015-04-29
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Amazon
- **Affected Products:** App Store
- **Credit:** MWR Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-160/
## Vulnerability Details

This vulnerability allows remote attackers to transmit unencrypted traffic on the Amazon App Store. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. All the HTML content within the Amazon App Store is transmitted over HTTPS and URIMatchers. The URIMatchers do not limit traffic to only HTTPS; Therefore, it is possible to request traffic over HTTP. An attacker can chain this vulnerability with other vulnerabilities to install malicious applications.

## Additional Details

There was not an advisory posted and no patch required, the issue was fixed server side.

## Disclosure Timeline

- 2014-11-12 - Vulnerability reported to vendor
- 2015-04-29 - Coordinated public release of advisory
