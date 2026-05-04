# ZDI-10-248: Apple Mac OS X IPv6 PIM Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-248
- **ZDI-CAN:** ZDI-CAN-857
- **Date:** 2010-11-10
- **CVE:** CVE-2010-1843
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:N/A:C
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-248/
## Vulnerability Details

This vulnerability allows remote attackers to denial of service the IPv6 stack of an installation of Apple Mac OSX. No authentication or user interaction is required in order to exploit this vulnerability. The specific flaw exists within OSX's IPv6 stack. A NULL pointer dereference vulnerability was discovered in the xnu kernel implementation when a specially formatted packet is sent to it. Exploiting this vulnerability will result in a remote denial of service against the target os.

## Additional Details

Mac OS X 10.6.5: http://support.apple.com/kb/HT4435 iOS 4.2: http://support.apple.com/kb/HT4456

## Disclosure Timeline

- 2010-08-17 - Vulnerability reported to vendor
- 2010-11-10 - Coordinated public release of advisory
