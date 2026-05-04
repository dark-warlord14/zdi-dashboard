# ZDI-19-285: (0Day) (Pwn2Own) Xiaomi Mi6 Browser market.install apkPath Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-285
- **ZDI-CAN:** ZDI-CAN-7484
- **Date:** 2019-03-15
- **CVE:** N/A
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Xiaomi
- **Affected Products:** Browser
- **Credit:** MWR Labs - Georgi Geshev and Robert Miller
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-285/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Xiaomi Mi6 Browser. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the apkPath parameter. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 11/14/18 - ZDI reported vulnerability to vendor 11/14/18 - Vendor acknowledged 01/27/19 - ZDI contacted vendor requesting a status update 02/06/19 - ZDI contacted vendor again requesting a status update 02/06/19 - Vendor replied stating they plan to publish an update by the end of February 02/08/19 - ZDI notified the vendor the case would be 0-dayed if a fix was not available by the end of February 03/04/19 - Vendor replied but did not provide ETA 03/06/19 - ZDI notified the vendor the intention to 0-day the reports -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2018-11-15 - Vulnerability reported to vendor
- 2019-03-15 - Coordinated public release of advisory
- 2020-01-15 - Advisory Updated
