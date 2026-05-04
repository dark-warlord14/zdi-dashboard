# ZDI-19-124: (Pwn2Own) Apple Safari RegExp JIT Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-124
- **ZDI-CAN:** ZDI-CAN-7473
- **Date:** 2019-01-24
- **CVE:** CVE-2019-6217
- **CVSS:** 6.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** flouroacetate
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-124/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of regular expressions. By performing actions in JavaScript, an attacker can trigger a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/kb/HT201222

## Disclosure Timeline

- 2018-11-15 - Vulnerability reported to vendor
- 2019-01-24 - Coordinated public release of advisory
- 2019-06-14 - Advisory Updated
