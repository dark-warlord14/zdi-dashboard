# ZDI-17-151: Trend Micro Deep Discovery Email Inspector db_export Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-151
- **ZDI-CAN:** ZDI-CAN-4333
- **Date:** 2017-03-09
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Trend Micro
- **Affected Products:** Deep Discovery Email Inspector
- **Credit:** Brian Gorenc - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-151/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Trend Micro Deep Discovery Email Inspector. Authentication is not required to exploit this vulnerability. The specific flaw exists within db_export.php. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code under the context of root.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1116750

## Disclosure Timeline

- 2017-01-05 - Vulnerability reported to vendor
- 2017-03-09 - Coordinated public release of advisory
