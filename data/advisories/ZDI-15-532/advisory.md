# ZDI-15-532: SAP 3D Visual Enterprise Viewer Filmbox document Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-532
- **ZDI-CAN:** ZDI-CAN-2978
- **Date:** 2015-10-20
- **CVE:** CVE-2015-8029
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** SAP
- **Affected Products:** 3D Visual Enterprise Viewer
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-532/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of SAP 3D Visual Enterprise Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Filmbox documents. With a specially crafted Filmbox document, an attacker can trigger a memory corruption condition. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

The vendor advised ZDI that the patch and notes will be visible to customers on 13th of October 2015.

## Disclosure Timeline

- 2015-07-09 - Vulnerability reported to vendor
- 2015-10-20 - Coordinated public release of advisory
