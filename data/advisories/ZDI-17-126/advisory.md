# ZDI-17-126: Trend Micro SafeSync for Enterprise license Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-126
- **ZDI-CAN:** ZDI-CAN-4403
- **Date:** 2017-03-01
- **CVE:** N/A
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Trend Micro
- **Affected Products:** SafeSync for Enterprise
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-126/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Trend Micro SafeSync for Enterprise. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the license endpoint. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code under the context of root.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1116749

## Disclosure Timeline

- 2017-02-02 - Vulnerability reported to vendor
- 2017-03-01 - Coordinated public release of advisory
