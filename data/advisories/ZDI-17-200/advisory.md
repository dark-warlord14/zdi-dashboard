# ZDI-17-200: Trend Micro InterScan Web Security Virtual Appliance WmiDCDetector getAdHost Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-200
- **ZDI-CAN:** ZDI-CAN-4325
- **Date:** 2017-03-29
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Trend Micro
- **Affected Products:** InterScan Web Security Virtual Appliance
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-200/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Trend Micro InterScan Web Security Virtual Appliance. Authentication is not required to exploit this vulnerability. The specific flaw exists within WmiDCDetector's getADHost method. A crafted domain parameter can trigger execution of a system call composed from a user-supplied string. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current user.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1116960

## Disclosure Timeline

- 2016-12-20 - Vulnerability reported to vendor
- 2017-03-29 - Coordinated public release of advisory
