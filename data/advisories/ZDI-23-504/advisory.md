# ZDI-23-504: Delta Electronics DIAScreen DPA File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-504
- **ZDI-CAN:** ZDI-CAN-19212
- **Date:** 2023-05-01
- **CVE:** CVE-2023-0250
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Electronics
- **Affected Products:** DIAScreen
- **Credit:** Natnael Samson (@NattiSamson)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-504/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Delta Electronics DIAScreen. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DPA files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-23-033-01

## Disclosure Timeline

- 2022-11-10 - Vulnerability reported to vendor
- 2023-05-01 - Coordinated public release of advisory
