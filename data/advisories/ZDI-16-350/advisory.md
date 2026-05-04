# ZDI-16-350: Trend Micro InterScan Web Security Virtual Appliance wmi_domain_controllers Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-350
- **ZDI-CAN:** ZDI-CAN-3514
- **Date:** 2016-05-20
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Trend Micro
- **Affected Products:** InterScan Web Security
- **Credit:** Brian Gorenc - HPE Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-350/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Trend Micro InterScan Web Security. Authentication is not required to exploit this vulnerability. The specific flaw exists within processing of the /rest/wmi_domain_controllers requests. Multiple parameters required for the request are subject to command injection. An attacker can leverage this vulnerability to execute arbitrary commands in the context of the process.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: http://esupport.trendmicro.com/solution/en-US/1114185.aspx

## Disclosure Timeline

- 2016-01-22 - Vulnerability reported to vendor
- 2016-05-20 - Coordinated public release of advisory
