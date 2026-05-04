# ZDI-17-500: Trend Micro Control Manager cmdHandlerFileHandling Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-500
- **ZDI-CAN:** ZDI-CAN-4684
- **Date:** 2017-07-31
- **CVE:** CVE-2017-11389
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Trend Micro
- **Affected Products:** Control Manager
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-500/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Trend Micro Control Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within cmdHandlerFileHandling.dll. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute arbitrary code under the context of the iusr account.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1117722

## Disclosure Timeline

- 2017-04-05 - Vulnerability reported to vendor
- 2017-07-31 - Coordinated public release of advisory
