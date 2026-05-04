# ZDI-17-774: Trend Micro Mobile Security for Enterprise Proxy Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-774
- **ZDI-CAN:** ZDI-CAN-4681
- **Date:** 2017-09-15
- **CVE:** CVE-2017-14081
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/Au:S/C:P/I:P/A:P
- **Affected Vendors:** Trend Micro
- **Affected Products:** Mobile Security for Enterprise
- **Credit:** Steven Seeley (mr_me) of Offensive Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-774/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Trend Micro Mobile Security for Enterprise. Authentication is required to exploit this vulnerability. The specific flaw exists within the modTMCSS Proxy functionality. When parsing certain parameters and "type" is set to "WR," the process does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1118224

## Disclosure Timeline

- 2017-06-27 - Vulnerability reported to vendor
- 2017-09-15 - Coordinated public release of advisory
