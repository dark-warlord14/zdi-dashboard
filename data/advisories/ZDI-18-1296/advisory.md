# ZDI-18-1296: Trend Micro Anti-Virus KERedirect Untrusted Pointer Dereference Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1296
- **ZDI-CAN:** ZDI-CAN-6371
- **Date:** 2018-10-19
- **CVE:** CVE-2018-18328
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Trend Micro
- **Affected Products:** Anti-Virus
- **Credit:** vms
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1296/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Trend Micro Anti-Virus. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the KERedirect kext. The issue results from the lack of proper validation of a user-supplied value prior to dereferencing it as a pointer. An attacker can leverage this vulnerability to execute code in the context of the kernel.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://esupport.trendmicro.com/en-US/home/pages/technical-support/1121296.aspx

## Disclosure Timeline

- 2018-06-22 - Vulnerability reported to vendor
- 2018-10-19 - Coordinated public release of advisory
- 2018-10-19 - Advisory Updated
