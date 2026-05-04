# ZDI-23-1045: (0Day) Inductive Automation Ignition AbstractGatewayFunction Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1045
- **ZDI-CAN:** ZDI-CAN-17587
- **Date:** 2023-08-08
- **CVE:** CVE-2023-39473
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Inductive Automation
- **Affected Products:** Ignition
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1045/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Inductive Automation Ignition. Authentication is required to exploit this vulnerability. The specific flaw exists within the AbstractGatewayFunction class. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

06/06/22 – ZDI reported the vulnerability to the vendor. 06/06/22 – The vendor acknowledged the report. 12/20/22 – The ZDI asked for an update. 12/20/22 – The vendor states they requested an update from engineering. 12/22/22 – The vendor states that they are working on a patch. 07/18/23 – The ZDI asked for an update. 07/21/23 – The vendor states that the case is still in active development. 08/01/23 – ZDI informed the vendor that the case will be published as a zero-day advisory on 08/08/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2022-06-06 - Vulnerability reported to vendor
- 2023-08-08 - Coordinated public release of advisory
- 2023-08-08 - Advisory Updated
