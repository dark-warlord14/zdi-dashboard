# ZDI-13-287: (Mobile Pwn2Own) Samsung Apps/WatchON WebView JavaScript Bridge Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-287
- **ZDI-CAN:** ZDI-CAN-2052
- **Date:** 2013-12-31
- **CVE:** CVE-2013-7396
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Samsung
- **Affected Products:** Apps/WatchON
- **Credit:** Mitsui Bussan Secure Directions, Inc.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-287/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Samsung Apps and Samsung WatchOn. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the WebView JavaScript Bridge. The issue lies in the ability to execute arbitrary commands from JavaScript. This can be chained with the ability to install arbitrary packages to execute code under the context of the current user.

## Additional Details

Samsung has issued the following updates to Samsung Apps and WatchOn. * WatchON version 13122001.1.21.60 (Phone, patch made available since 12/31/2013)/13112601.1.51.21 (Tablet, patch made available since 12/31/2013) or later version * Samsung Apps 13121804.12025.0 (patch made available since 12/31/2013) or later version In addition, Samsung has continued to issue, or is in the process of scheduling with the carriers, the updates to the defective class as well since 12/03/2013. The patch date may vary due to the schedule of carrier. Please contact us ( m.security@samsung.com ) if you would like to know the status of the update for your Samsung device. NOTE: Samsung Galaxy devices running Kitkat are not affected by these vulnerabilities.

## Disclosure Timeline

- 2013-11-13 - Vulnerability reported to vendor
- 2013-12-31 - Coordinated public release of advisory
