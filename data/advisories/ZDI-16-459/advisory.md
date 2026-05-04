# ZDI-16-459: Trend Micro Control Manager DeploymentPlan_Event_Handler External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-459
- **ZDI-CAN:** ZDI-CAN-3639
- **Date:** 2016-08-09
- **CVE:** N/A
- **CVSS:** 4.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:P/I:N/A:N
- **Affected Vendors:** Trend Micro
- **Affected Products:** Control Manager
- **Credit:** k0rpr1t_z0mb1e
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-459/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Trend Micro Control Manager. Authentication is required to exploit this vulnerability. The specific flaw exists within DeploymentPlan_Event_Handler.aspx. The issue lies in the failure to sanitize user-supplied input prior to parsing it as XML. An attacker can use this information in conjunction with other vulnerabilities to execute code in the context of the process.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: http://esupport.trendmicro.com/solution/en-US/1114749.aspx

## Disclosure Timeline

- 2016-03-29 - Vulnerability reported to vendor
- 2016-08-09 - Coordinated public release of advisory
