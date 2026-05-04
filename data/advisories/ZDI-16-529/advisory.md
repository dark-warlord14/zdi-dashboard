# ZDI-16-529: Trend Micro Maximum Security tmnciesc driver Untrusted Pointer Dereference Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-529
- **ZDI-CAN:** ZDI-CAN-3843
- **Date:** 2016-10-06
- **CVE:** N/A
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Trend Micro
- **Affected Products:** Maximum Security
- **Credit:** Jaanus Kp Clarified Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-529/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Trend Micro Maximum Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the processing of IOCTL 0x00222813 by the tmnciesc device driver. The issue lies in the failure to validate a user-supplied value prior to dereferencing it as a pointer. An attacker can leverage this vulnerability to execute arbitrary code under the context of the kernel.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://esupport.trendmicro.com/en-us/home/pages/technical-support/1115282.aspx

## Disclosure Timeline

- 2016-07-12 - Vulnerability reported to vendor
- 2016-10-06 - Coordinated public release of advisory
