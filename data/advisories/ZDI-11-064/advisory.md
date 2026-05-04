# ZDI-11-064: Microsoft Windows WmiTraceMessageVa Local Kernel Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-064
- **ZDI-CAN:** ZDI-CAN-890
- **Date:** 2011-02-08
- **CVE:** CVE-2011-0045
- **CVSS:** 6.8
- **CVSS Vector:** AV:L/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows XP
- **Credit:** std_logic
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-064/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code from the context of kernelspace on vulnerable installations of Microsoft Windows. The ability to make a system call is required in order to exploit this vulnerability. The specific flaw exists within the kernel's support for Trace Events. Due to a bad type conversion, the kernel will use a truncated length for allocating data from userspace. When populating this buffer the kernel will use a differing length causing a buffer overflow. This will cause memory corruption and can lead to code execution under the context of the kernel.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms11-011.mspx

## Disclosure Timeline

- 2010-09-29 - Vulnerability reported to vendor
- 2011-02-08 - Coordinated public release of advisory
