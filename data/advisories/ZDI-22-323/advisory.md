# ZDI-22-323: Schneider Electric IGSS IGSSdataServer Uninitialized Memory Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-323
- **ZDI-CAN:** ZDI-CAN-15119
- **Date:** 2022-02-11
- **CVE:** CVE-2022-24316
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Schneider Electric
- **Affected Products:** IGSS
- **Credit:** Vyacheslav Moskvin
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-323/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Schneider Electric IGSS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the IGSSDataServer process, which listens on TCP port 12401 by default. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the IGSSDataServer process.

## Additional Details

https://download.schneider-electric.com/files?p_Doc_Ref=SEVD-2022-039-01 https://www.cisa.gov/uscert/ics/advisories/icsa-22-046-01

## Disclosure Timeline

- 2021-12-15 - Vulnerability reported to vendor
- 2022-02-11 - Coordinated public release of advisory
- 2023-09-20 - Advisory Updated
