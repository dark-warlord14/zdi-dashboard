# ZDI-23-891: (0Day) ManageEngine ADSelfService Plus GINA Client Insufficient Verification of Data Authenticity Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-891
- **ZDI-CAN:** ZDI-CAN-17009
- **Date:** 2023-06-21
- **CVE:** CVE-2023-35719
- **CVSS:** 6.8
- **CVSS Vector:** AV:P/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** ManageEngine
- **Affected Products:** ADSelfService Plus
- **Credit:** Pedro Ribeiro (pedrib@gmail.com | @pedrib1337), João Bigotte and Ashley King from Agile Information Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-891/
## Vulnerability Details

This vulnerability allows physically present attackers to execute arbitrary code on affected installations of ManageEngine ADSelfService Plus. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Password Reset Portal used by the GINA client. The issue results from the lack of proper authentication of data received via HTTP. An attacker can leverage this vulnerability to bypass authentication and execute code in the context of SYSTEM.

## Additional Details

04/29/22 – The ZDI reported the vulnerability to the vendor. 05/01/22 – The vendor acknowledged the report. 07/13/22 – The vendor asked for additional details. 07/13/22 – The ZDI provided additional details. 08/09/22 – The vendor states they are investigating the report. 08/09/22 – The vendor asked for additional details. 08/09/22 – The ZDI provided additional details. 09/13/22 – The vendor states this vulnerability can be mitigated using the best practices. 04/19/23 – The ZDI asked for an update. 04/19/23 – The vendor states that following the best practice guidelines will mitigate this vulnerability and that they would consider adding user alerts in a future release. 06/08/23 – The ZDI conducted a review, and we determined that the product is still vulnerable even with best practices implemented. 06/13/23 – The ZDI informed the vendor of our findings and that the case will be published as a zero-day advisory on 06/21/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2022-04-29 - Vulnerability reported to vendor
- 2023-06-21 - Coordinated public release of advisory
