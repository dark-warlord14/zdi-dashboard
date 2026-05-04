# ZDI-18-999: (0Day) Hewlett Packard Enterprise Intelligent Management Center imcwlandm strUserName Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-999
- **ZDI-CAN:** ZDI-CAN-5672
- **Date:** 2018-09-07
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** sztivi
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-999/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett Packard Enterprise Intelligent Management Center. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of the dealInodeOfflineMsg message. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code under the context of SYSTEM.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 02/23/18 - ZDI reported 1st vulnerability to vendor 02/23/18 - Vendor acknowledged and provided ZDI with a ticket number 03/02/18 - ZDI reported 2nd vulnerability to vendor 03/09/18 - Vendor contacted ZDI requesting additional details on the cases 03/21/18 - ZDI provided vendor the requested information 07/20/18 - Vendor provided an update on other released cases but no update on the cases involved 07/23/18 - ZDI contacted vendor requesting an update and mentioning the intention to 0-day them 08/17/18 - ZDI contacted vendor again requesting an update 08/21/18 - Vendor replied they would release the fix on August 30 and requested to hold the 0-day 08/21/18 - ZDI contacted vendor confirming an extension until August 30 08/31/18 - ZDI contacted vendor asking for release details as nothing was apparently published 09/02/18 - ZDI notified vendor these cases will 0-day on Friday September 7 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting.

## Disclosure Timeline

- 2018-02-23 - Vulnerability reported to vendor
- 2018-09-07 - Coordinated public release of advisory
- 2018-09-07 - Advisory Updated
