# ZDI-14-263: (0Day) Hewlett-Packard Data Protector Cell Request Service Opcode 1091 Directory Traversal Arbitrary File Write Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-263
- **ZDI-CAN:** ZDI-CAN-2170
- **Date:** 2014-07-23
- **CVE:** CVE-2014-5160
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Data Protector
- **Credit:** Aniway.Anyway@gmail.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-263/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard Data Protector. Authentication is not required to exploit this vulnerability. The specific flaw exists within crs.exe which listens by default on a random TCP port. When parsing opcode 1091, the process is vulnerable to directory traversal leading to creation of an arbitrary file . A remote attacker can chain this with another vulnerability to execute remote code under the context of the user running Data Protector.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 03/07/2014 - Disclosed to vendor 03/26/2014 - Vendor response: 'by design' 03/27/2014 - Vendor elaborates: 'by design' (ZDI has historically disagreed with this stance as the design is insecure) 05/30/2014 - ZDI notifies of upcoming 120-days and confirms that vendor stance remains the same 05/30/2014 - Confirmation from vendor 06/11/2014 - ZDI notifies of intent to 0-day 07/23/2014 - Public release of advisory -- Vendor Mitigation: You can enable the encrypted control communication from the command line as root be doing the following. Please review your configuration and enable it from the command line interface, executing: # omnicc -encryption -enable You can read up on the capability on page 145 of the User Guide. That guide is a PDF file, and found in /opt/omni/doc/C If you have further questions regarding enabling ECC on Data Protector, open a support call with the appropriate product specialists. -- Mitigation: Given the stated purpose of Data Protector, and the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the HP Data Protector service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting. These features are available in the native Windows Firewall, as described in http://technet.microsoft.com/en-us/library/cc725770%28WS.10%29.aspx and numerous other Microsoft Knowledge Base articles.

## Disclosure Timeline

- 2014-03-07 - Vulnerability reported to vendor
- 2014-07-23 - Coordinated public release of advisory
