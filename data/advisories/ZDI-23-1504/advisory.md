# ZDI-23-1504: (0Day) D-Link DAP-1325 SetAPLanSettings DeviceName Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1504
- **ZDI-CAN:** ZDI-CAN-18825
- **Date:** 2023-10-04
- **CVE:** CVE-2023-44406
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DAP-1325
- **Credit:** Dmitry "InfoSecDJ" Janushkevich of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1504/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of D-Link DAP-1325 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of XML data provided to the HNAP1 SOAP endpoint. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

09/26/22 – ZDI reported the vulnerability to the vendor. 08/25/23 – ZDI asked for an update. 08/30/23 – The vendor states the issues in DAP-1325 should be addressed in a previous update. 08/31/23 – ZDI informed the vendor that these cases were not included in the update. 09/29/23 – The ZDI informed the vendor that the case will be published as a zero-day advisory on 10/04/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2022-09-26 - Vulnerability reported to vendor
- 2023-10-04 - Coordinated public release of advisory
