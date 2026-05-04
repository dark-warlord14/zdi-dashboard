# ZDI-23-511: Delta Electronics DIAScreen DPA File Parsing Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-511
- **ZDI-CAN:** ZDI-CAN-19433
- **Date:** 2023-05-01
- **CVE:** CVE-2023-0251
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Electronics
- **Affected Products:** DIAScreen
- **Credit:** YuLin Sung of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-511/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Delta Electronics DIAScreen. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DPA files. Crafted data in an RTC section can trigger an overflow of a buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-23-033-01

## Disclosure Timeline

- 2022-11-11 - Vulnerability reported to vendor
- 2023-05-01 - Coordinated public release of advisory
