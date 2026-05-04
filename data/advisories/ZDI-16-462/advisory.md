# ZDI-16-462: Trend Micro Control Manager task_controller Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-462
- **ZDI-CAN:** ZDI-CAN-3709
- **Date:** 2016-08-09
- **CVE:** N/A
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Trend Micro
- **Affected Products:** Control Manager
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-462/
## Vulnerability Details

This vulnerability allows remote attackers to leak sensitive information on vulnerable installations of Trend Micro Control Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within task_controller.php. The url parameter does not properly sanitize the path supplied. An attacker can leverage this vulnerability to disclose arbitrary files from the system.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: http://esupport.trendmicro.com/solution/en-US/1114749.aspx

## Disclosure Timeline

- 2016-05-10 - Vulnerability reported to vendor
- 2016-08-09 - Coordinated public release of advisory
