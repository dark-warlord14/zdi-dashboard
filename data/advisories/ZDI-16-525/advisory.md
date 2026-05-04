# ZDI-16-525: (0Day) Fatek Automation PM Designer Heap Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-525
- **ZDI-CAN:** ZDI-CAN-3586
- **Date:** 2016-09-21
- **CVE:** N/A
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Fatek Automation
- **Affected Products:** PM Designer
- **Credit:** Ariele Caltabiano (kimiya)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-525/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Fatek Automation PM Designer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within parsing of a pm3 file. A malformed file can lead to heap memory corruption. A remote attacker can leverage this vulnerability to cause arbitrary code execution in the context of the user.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 03/03/2016 - ZDI disclosed the vulnerability to ICS-CERT to coordinate with the vendor 03/04/2016 - ICS-CERT acknowledged and provided ZDI with an ICS-VU case number 08/24/2016 - ZDI inquired with ICS-CERT whether we had missed the patch 08/25/2016 - ICS-CERT confirmed contact with the vendor but indicated there was no patch yet 08/30/2016 - ICS-CERT advised ZDI that they had no confirmation of a patch from the vendor 08/30/2016 - ZDI informed ICS-CERT that this will publish this as 0-day on 09/19/2016 09/20/2016 - ZDI spoke to ICS-CERT by phone to confirm the 0-day report details and that the 0-day will post this week -- Mitigation: Given the stated purpose of Fatek Automation PM Designer, and the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2016-03-03 - Vulnerability reported to vendor
- 2016-09-21 - Coordinated public release of advisory
