# ZDI-16-530: Trend Micro Maximum Security tmnciesc Kernel Driver Memory Corruption Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-530
- **ZDI-CAN:** ZDI-CAN-3827
- **Date:** 2016-10-06
- **CVE:** N/A
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Trend Micro
- **Affected Products:** Maximum Security
- **Credit:** bee13oy of CloverSec Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-530/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Trend Micro Maximum Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the processing of IOCTL 0x0022205c by the tmnciesc kernel driver. The issue lies in the failure to properly validate user-supplied data which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute arbitrary code under the context of kernel.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://esupport.trendmicro.com/en-us/home/pages/technical-support/1115282.aspx

## Disclosure Timeline

- 2016-06-21 - Vulnerability reported to vendor
- 2016-10-06 - Coordinated public release of advisory
