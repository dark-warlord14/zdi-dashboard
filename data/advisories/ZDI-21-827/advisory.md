# ZDI-21-827: Microsoft Visual Studio Code maven.executable.options Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-827
- **ZDI-CAN:** ZDI-CAN-13463
- **Date:** 2021-07-19
- **CVE:** CVE-2021-34529
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Visual Studio Code
- **Credit:** Kc Udonsi (@glitchnsec) of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-827/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Visual Studio Code. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of the settings.json file. When parsing the maven.executable.options parameter, the process does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34529

## Disclosure Timeline

- 2021-03-17 - Vulnerability reported to vendor
- 2021-07-19 - Coordinated public release of advisory
