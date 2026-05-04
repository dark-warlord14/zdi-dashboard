# ZDI-17-080: Trend Micro Control Manager TreeUserControl_process_tree_event XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-080
- **ZDI-CAN:** ZDI-CAN-4151
- **Date:** 2017-09-22
- **CVE:** N/A
- **CVSS:** 4.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:P/I:N/A:N
- **Affected Vendors:** Trend Micro
- **Affected Products:** Control Manager
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-080/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Trend Micro Control Manager. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within TreeUserControl_process_tree_event.aspx. This page exhibits an XML external entity injection vulnerability. An attacker can leverage this vulnerability to disclose sensitive information under the context of NETWORKSERVICE.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1116624

## Disclosure Timeline

- 2016-11-23 - Vulnerability reported to vendor
- 2017-09-22 - Coordinated public release of advisory
