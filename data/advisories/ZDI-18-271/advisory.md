# ZDI-18-271: Apple Safari Spread Operator Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-271
- **ZDI-CAN:** ZDI-CAN-5558
- **Date:** 2018-04-06
- **CVE:** CVE-2018-4122
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** WanderingGlitch - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-271/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of JIT. By performing actions in JavaScript, an attacker can trigger a type confusion condition. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/kb/HT201222

## Disclosure Timeline

- 2018-01-02 - Vulnerability reported to vendor
- 2018-04-06 - Coordinated public release of advisory
- 2018-04-06 - Advisory Updated
