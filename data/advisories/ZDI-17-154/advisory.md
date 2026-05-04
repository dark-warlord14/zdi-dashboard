# ZDI-17-154: Trend Micro Deep Discovery Email Inspector reboot_after_hotfix Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-154
- **ZDI-CAN:** ZDI-CAN-4347
- **Date:** 2017-03-09
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:N/A:C
- **Affected Vendors:** Trend Micro
- **Affected Products:** Deep Discovery Email Inspector
- **Credit:** Brian Gorenc - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-154/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial of service condition on vulnerable installations of Trend Micro Deep Discovery Email Inspector. Authentication is not required to exploit this vulnerability. The specific flaw exists within reboot_after_hotfix.php. The issue results from the lack of authentication around critical functionality resulting in a system reboot. An attacker can leverage this vulnerability to disable the service provided by the product.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1116750

## Disclosure Timeline

- 2017-01-05 - Vulnerability reported to vendor
- 2017-03-09 - Coordinated public release of advisory
