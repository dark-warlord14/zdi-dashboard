# ZDI-22-543: KOYO Screen Creator SCA2 File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-543
- **ZDI-CAN:** ZDI-CAN-14868
- **Date:** 2022-03-29
- **CVE:** CVE-2022-27648
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** KOYO
- **Affected Products:** Screen Creator
- **Credit:** Tran Van Khang - khangkito (VinCSS)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-543/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of KOYO Screen Creator. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SCA2 files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

KOYO has issued an update to correct this vulnerability. More details can be found at: https://www.koyoele.co.jp/en/topics/202203154994/

## Disclosure Timeline

- 2021-12-03 - Vulnerability reported to vendor
- 2022-03-29 - Coordinated public release of advisory
