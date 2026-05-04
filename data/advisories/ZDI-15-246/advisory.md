# ZDI-15-246: (0Day) Wavelink Emulation ConnectPro TermProxy WLTermProxyService.exe HTTP Request Headers Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-246
- **ZDI-CAN:** ZDI-CAN-2720
- **Date:** 2015-05-27
- **CVE:** CVE-2015-4060
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Wavelink
- **Affected Products:** ConnectPro
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-246/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Wavelink Emulation ConnectPro TermProxy. User interaction is not required to exploit this vulnerability. The specific flaw exists in the parsing of HTTP requests in WLTermProxyService.exe listening by default on port 4428. When parsing large HTTP headers, the application will overflow a heap buffer due to an unsafe memory block copy operation. An attacker could leverage this to execute arbitrary code in the context of SYSTEM.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI vulnerability disclosure policy on lack of vendor response. ~2/20/2015 - ZDI called Wavelink customer service and a recorded message indicated these products are supported by another entity 02/20/2015 - ZDI reached out to multiple security contacts at that entity looking for a contact and familiarity with the product but received a negative reply The finder reached out to ZDI to say that there was some indication another entity was supporting these products. 04/09/2015 - ZDI reached out to security contacts at the 3rd party looking for a contact and familiarity with the product but received no reply 04/15/2015 - ZDI reached out to security contacts at the 3rd party looking for a contact and familiarity with the product but received no reply 05/20/2015 - ZDI reached out to security@wavelink.com , secure@wavelink.com and support@wavelink.com but received only an automated reply 05/20/2015 - ZDI again reached out to security contacts at the 3rd party looking for a contact and familiarity with the product but received a no reply The finder has also made attempts at contact with the vendor/owner regarding these vulnerability reports, but has made no meaningful contact. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting. These features are available in the native Windows Firewall, as described in http://technet.microsoft.com/en-us/library/cc725770%28WS.10%29.aspx and numerous other Microsoft Knowledge Base articles.

## Disclosure Timeline

- 2015-02-20 - Vulnerability reported to vendor
- 2015-05-27 - Coordinated public release of advisory
