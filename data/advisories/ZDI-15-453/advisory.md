# ZDI-15-453: (0Day) Moxa OnCell Central Manager Server RequestController Static Credentials Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-453
- **ZDI-CAN:** ZDI-CAN-2529
- **Date:** 2015-09-29
- **CVE:** CVE-2015-6481
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Moxa
- **Affected Products:** OnCell Central Manager
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-453/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Moxa OnCell Central Manager Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the RequestController class. The specific flaw exists within the login() function which contains hard-coded credentials. An attacker can exploit this condition to take full control of the product and achieve code execution on all managed hosts.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI vulnerability disclosure policy on lack of vendor response. 02/05/2015 - ZDI sent reports to ICS-CERT 02/09/2015 - ZDI receieved an ACK and ticket # from ICS-CERT 04/14/2015 - ZDI recieved an update from ICS-CERT that these cases were in work, but "months out" 04/15/2015 - ZDI reminded ISC-CERT of the prediacted disclosure date, but indicated some flexibility if the vendor could come close 05/14/2015 - ICS-CERT advised ZDI that the vendor could not patch until August 05/14/2015 - ZDI agreed to go out to August 5 09/14/2015 - After getting a response that other Moxa cases had patched, but seemingly not these, ZDI asked ICS-CERT if these did not patch with the August 27 patch 09/15/2015 - ICS-CERT indicated that they would reach out to the vendor for clarification and requested extension to do so. ZDI declined an extension, but indicated we "will wait a couple of days, for a status." 09/18/2015 - ZDI notified ICS-CERT of the intent to 0-day the reports -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting. These features are available in the native Windows Firewall, as described in http://technet.microsoft.com/en-us/library/cc725770%28WS.10%29.aspx and numerous other Microsoft Knowledge Base articles. -- Vendor Patch: See https://ics-cert.us-cert.gov/advisories/ICSA-15-328-01

## Disclosure Timeline

- 2015-02-05 - Vulnerability reported to vendor
- 2015-09-29 - Coordinated public release of advisory
