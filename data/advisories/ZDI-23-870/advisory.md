# ZDI-23-870: (0Day) Ashlar-Vellum Cobalt Uninitialized Memory Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-870
- **ZDI-CAN:** ZDI-CAN-19878
- **Date:** 2023-06-15
- **CVE:** CVE-2023-34310
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ashlar-Vellum
- **Affected Products:** Cobalt
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-870/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ashlar-Vellum Cobalt. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of CO files. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

01/11/23 – ZDI reported the vulnerability to the vendor. 01/12/23 – The vendor acknowledged the report. 06/07/23 – The ZDI asked for an update. 06/08/23 – The vendor states that the vulnerability would be fixed in a future build. 06/08/23 – The ZDI informed the vendor that the case will be published as a zero-day advisory on 06/15/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-01-11 - Vulnerability reported to vendor
- 2023-06-15 - Coordinated public release of advisory
