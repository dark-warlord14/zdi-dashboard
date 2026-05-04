# ZDI-17-213: Trend Micro InterScan Web Security Virtual Appliance ConfigIPNetwork saveNetworkConfiguration dataPingChanged Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-213
- **ZDI-CAN:** ZDI-CAN-4270
- **Date:** 2017-03-30
- **CVE:** N/A
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Trend Micro
- **Affected Products:** InterScan Web Security Virtual Appliance
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-213/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Trend Micro InterScan Web Security Virtual Appliance. Authentication is required to exploit this vulnerability. The specific flaw exists within ConfigIPNetwork's saveNetworkConfiguration method. A crafted inEth parameter can trigger execution of a system call composed from a user-supplied string. An attacker can leverage this vulnerability to execute arbitrary code under the context of root.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1116960

## Disclosure Timeline

- 2016-12-19 - Vulnerability reported to vendor
- 2017-03-30 - Coordinated public release of advisory
