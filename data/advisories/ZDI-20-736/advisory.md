# ZDI-20-736: (0Day) NEC ESMPRO Manager GetEuaLogDownloadAction Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-736
- **ZDI-CAN:** ZDI-CAN-9607
- **Date:** 2020-06-25
- **CVE:** CVE-2020-27859
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** NEC
- **Affected Products:** ESMPRO Manager
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-736/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of NEC ESMPRO Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the GetEuaLogDownloadAction class. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose information in the context of SYSTEM.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 01/16/20 - ZDI reported the vulnerability to JP-CERT 01/21/20 - JP-CERT confirmed receipt of the report 04/30/20 - ZDI requested an update 05/07/20 - JP-CERT replied that the vendor said the report did not meet the bar for security servicing 05/07/20 - ZDI provided additional evidence 05/14/20 - JP-CERT confirmed receipt of the ZDI response 05/28/20 - ZDI contacted JP-CERT requesting a status update 06/01/20 - JP-CERT requested an extension until 06/15/20 06/02/20 - ZDI agreed to the extension 06/04/20 - JP-CERT confirmed that a fix would be available by 06/15/20 06/12/20 - ZDI requested an update 06/15/20 - JP-CERT advised ZDI that a fix will be available by 09/30/20 06/16/20 - ZDI notified JP-CERT of the intention to publish these reports as 0-day advisories on 06/23/2020 11/10/20 - Vendor confirmed the issue was fixed in version 6.51 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting.

## Disclosure Timeline

- 2020-01-16 - Vulnerability reported to vendor
- 2020-06-25 - Coordinated public release of advisory
- 2020-12-04 - Advisory Updated
