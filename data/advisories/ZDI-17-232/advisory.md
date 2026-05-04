# ZDI-17-232: Trend Micro InterScan Web Security Virtual Appliance TestConfigure Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-232
- **ZDI-CAN:** ZDI-CAN-4324
- **Date:** 2017-03-30
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Trend Micro
- **Affected Products:** InterScan Web Security Virtual Appliance
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-232/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Trend Micro InterScan Web Security Virtual Appliance. Authentication is not required to exploit this vulnerability. The specific flaw exists within TestConfigure's test_configure method. A crafted parameter can trigger execution of a system call composed from a user-supplied string. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current user.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1116960

## Disclosure Timeline

- 2016-12-20 - Vulnerability reported to vendor
- 2017-03-30 - Coordinated public release of advisory
