# ZDI-18-268: Trend Micro Maximum Security tmnciesc Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-268
- **ZDI-CAN:** ZDI-CAN-5460
- **Date:** 2018-04-06
- **CVE:** CVE-2018-6234
- **CVSS:** 4.6
- **CVSS Vector:** AV:L/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Trend Micro
- **Affected Products:** Maximum Security
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-268/
## Vulnerability Details

This vulnerability allows local attackers disclose sensitive information on vulnerable installations of Trend Micro Maximum Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within processing of IOCTL 0x222814 by the tmnciesc.sys driver. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges to kernel.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://esupport.trendmicro.com/en-us/home/pages/technical-support/1119591.aspx

## Disclosure Timeline

- 2017-12-05 - Vulnerability reported to vendor
- 2018-04-06 - Coordinated public release of advisory
- 2018-04-06 - Advisory Updated
