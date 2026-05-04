# ZDI-17-504: Trend Micro InterScan Messaging Security Proxy Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-504
- **ZDI-CAN:** ZDI-CAN-4745
- **Date:** 2017-07-31
- **CVE:** CVE-2017-11392
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/Au:S/C:P/I:P/A:P
- **Affected Vendors:** Trend Micro
- **Affected Products:** InterScan Messaging Security
- **Credit:** Steven Seeley (mr_me) of Offensive Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-504/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Trend Micro InterScan Messaging Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the modTMCSS Proxy functionality. When parsing the "T" parameter, the process does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute arbitrary code under the context of the imss user.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1117723

## Disclosure Timeline

- 2017-06-27 - Vulnerability reported to vendor
- 2017-07-31 - Coordinated public release of advisory
