# ZDI-11-092: (0Day) Cisco Secure Desktop CSDWebInstaller ActiveX Control Cleaner.cab Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-092
- **ZDI-CAN:** ZDI-CAN-862
- **Date:** 2011-02-28
- **CVE:** CVE-2011-0925
- **CVSS:** 8.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Cisco
- **Affected Products:** Secure Desktop
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-092/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Cisco Secure Desktop. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within CSDWebInstaller.ocx. The CSDWebInstallerCtrl ActiveX control allows downloading and executing any Cisco-signed executable files. By renaming a Cisco-signed executable file to inst.exe and putting it on a webserver, an attacker can subsequently exploit vulnerabilities in the Cisco-signed executable file remotely.

## Additional Details

February 28, 2011 Vendor provided: http://tools.cisco.com/security/center/viewAlert.x?alertId=22528 --- February 23, 2011 - This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 180 day deadline. -- Mitigations: Cisco states that they will have a patch for this issue on March 31st, 2011. In the meantime, we suggest users implement the mitigations below. The killbit can be set on this control to disable scripting within Internet Explorer by modifying the data value of the Compatibilty Flags DWORD within the following location in the registry: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\ActiveX Compatibility\705EC6D4-B138-4079-A307-EF13E4889A82 If the Compatibility Flags value is set to 0x00000400 the control can no longer be instantiated inside the browser. For more information, please see: http://support.microsoft.com/kb/240797

## Disclosure Timeline

- 2010-08-25 - Vulnerability reported to vendor
- 2011-02-28 - Coordinated public release of advisory
