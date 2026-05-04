# ZDI-15-527: SAP 3D Visual Enterprise Viewer U3D Out-Of-Bounds Indexing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-527
- **ZDI-CAN:** ZDI-CAN-2986
- **Date:** 2015-10-20
- **CVE:** CVE-2015-8030
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** SAP
- **Affected Products:** 3D Visual Enterprise Viewer
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-527/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of SAP 3D Visual Enterprise Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of U3D files. The issue lies in the failure to ensure that index values are within the bounds of an allocated array. An attacker can leverage this vulnerability to execute arbitrary code within the context of the current process.

## Additional Details

The vendor advised ZDI that the patch and notes will be visible to customers on 13th of October 2015.

## Disclosure Timeline

- 2015-06-02 - Vulnerability reported to vendor
- 2015-10-20 - Coordinated public release of advisory
