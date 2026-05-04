# ZDI-17-243: Trend Micro Smart Protection Server wcs_bwlists_handler Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-243
- **ZDI-CAN:** ZDI-CAN-4242
- **Date:** 2017-04-05
- **CVE:** N/A
- **CVSS:** 8.5
- **CVSS Vector:** AV:N/AC:M/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Trend Micro
- **Affected Products:** Smart Protection Server
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-243/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Trend Micro Smart Protection Server. Authentication is required to exploit this vulnerability. The specific flaw exists within wcs_bwlists_handler.php. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute arbitrary code under the context of root.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1117033

## Disclosure Timeline

- 2017-01-10 - Vulnerability reported to vendor
- 2017-04-05 - Coordinated public release of advisory
