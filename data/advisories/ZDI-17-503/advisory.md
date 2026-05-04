# ZDI-17-503: Trend Micro Deep Discovery Email Inspector kdump_setting Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-503
- **ZDI-CAN:** ZDI-CAN-4350
- **Date:** 2017-07-31
- **CVE:** CVE-2017-11382
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:N/A:C
- **Affected Vendors:** Trend Micro
- **Affected Products:** Deep Discovery Email Inspector
- **Credit:** Brian Gorenc - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-503/
## Vulnerability Details

This vulnerability allows remote attackers to delete arbitrary files on vulnerable installations of Trend Micro Deep Discovery Email Inspector. Authentication is not required to exploit this vulnerability. The specific flaw exists within kdump_setting.php. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disable the service provided by the product.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1116750

## Disclosure Timeline

- 2017-01-05 - Vulnerability reported to vendor
- 2017-07-31 - Coordinated public release of advisory
