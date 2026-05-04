# ZDI-17-521: Trend Micro OfficeScan Proxy Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-521
- **ZDI-CAN:** ZDI-CAN-4544
- **Date:** 2017-08-02
- **CVE:** CVE-2017-11394
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Trend Micro
- **Affected Products:** OfficeScan
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-521/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Trend Micro OfficeScan. Authentication is required to exploit this vulnerability. The specific flaw exists within the Web Console, which listens on TCP port 4343 by default. When parsing the T parameter in Proxy.php, the process does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current service.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1117769

## Disclosure Timeline

- 2017-03-01 - Vulnerability reported to vendor
- 2017-08-02 - Coordinated public release of advisory
