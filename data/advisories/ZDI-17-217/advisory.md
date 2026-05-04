# ZDI-17-217: Trend Micro InterScan Web Security Virtual Appliance DomainList TestingADKerberos Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-217
- **ZDI-CAN:** ZDI-CAN-4375
- **Date:** 2017-03-30
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Trend Micro
- **Affected Products:** InterScan Web Security Virtual Appliance
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-217/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Trend Micro InterScan Web Security Virtual Appliance. Authentication is not required to exploit this vulnerability. The specific flaw exists within the DomainList's TestingADKerberos method. A crafted bdn parameter can trigger the execution of a system call composed from a user-supplied string. An attacker can leverage this vulnerability to execute arbitrary code under the context of the root.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1116960

## Disclosure Timeline

- 2017-01-03 - Vulnerability reported to vendor
- 2017-03-30 - Coordinated public release of advisory
