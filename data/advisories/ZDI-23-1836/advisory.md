# ZDI-23-1836: Linux Mint Xreader CBT File Parsing Argument Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1836
- **ZDI-CAN:** ZDI-CAN-22132
- **Date:** 2023-12-20
- **CVE:** CVE-2023-44452
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Linux Mint
- **Affected Products:** Xreader
- **Credit:** Febin Mon Saji
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1836/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Linux Mint Xreader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of CBT files. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Linux Mint has issued an update to correct this vulnerability. More details can be found at: https://github.com/linuxmint/xreader/commit/cd678889ecfe4e84a5cbcf3a0489e15a5e2e3736

## Disclosure Timeline

- 2023-09-27 - Vulnerability reported to vendor
- 2023-12-20 - Coordinated public release of advisory
