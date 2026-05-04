# ZDI-17-062: Trend Micro Control Manager download Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-062
- **ZDI-CAN:** ZDI-CAN-4006
- **Date:** 2017-02-07
- **CVE:** N/A
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Trend Micro
- **Affected Products:** Control Manager
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-062/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Trend Micro Control Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within widgets_new's download.php script. The issue lies in the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code under the context of the iusr account.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1116624

## Disclosure Timeline

- 2016-09-07 - Vulnerability reported to vendor
- 2017-02-07 - Coordinated public release of advisory
