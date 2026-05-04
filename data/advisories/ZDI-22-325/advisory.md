# ZDI-22-325: Schneider Electric IGSS IGSSDataServer Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-325
- **ZDI-CAN:** ZDI-CAN-15198
- **Date:** 2022-02-11
- **CVE:** CVE-2022-24313
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** IGSS
- **Credit:** Vyacheslav Moskvin
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-325/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Schneider Electric IGSS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the IGSSDataServer process, which listens on TCP port 12401 by default. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the IGSSDataServer process.

## Additional Details

https://download.schneider-electric.com/files?p_Doc_Ref=SEVD-2022-039-01 https://www.cisa.gov/uscert/ics/advisories/icsa-22-046-01

## Disclosure Timeline

- 2021-12-15 - Vulnerability reported to vendor
- 2022-02-11 - Coordinated public release of advisory
- 2023-09-20 - Advisory Updated
