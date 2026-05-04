# ZDI-15-062: (0Day) WebGate eDVR Manager WESPSerialPort.WESPSerialPortCtrl.1 Connect Method Stack Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-062
- **ZDI-CAN:** ZDI-CAN-2129
- **Date:** 2015-02-27
- **CVE:** CVE-2015-2097
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** WebGate
- **Affected Products:** eDVR Manager
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-062/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of WebGate eDVR Manager. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the WESPSerialPort.WESPSerialPortCtrl.1 control. The Connect method copies arbitrary data to a fixed-size stack buffer. This would allow an attacker to execute arbitrary code in the context of the browser.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 02/10/2014 - ZDI sent email to vendor requesting contact for disclosure 02/18/2014 - ZDI sent email to vendor requesting contact for disclosure 03/07/2014 - ZDI requested ICS-CERT assistance contacting the vendor 03/08/2014 - ZDI disclosed this case to ICS-CERT 05/12/2014 - ICS-CERT replied "We do not consider the WebGate eDVR Manager to be an element of control systems or of critical infrastructure, so we have forwarded these reports on to our friends at CERT/CC." ZDI has since sent multiple mails to ICS-CERT, CERT/CC and kn-cert@ncsc.go.kr regarding Webgate cases in general. However, to ZDI's knowledge, this has not resulted in any vendor response. -- Mitigation: The killbit can be set on this control to disable scripting within Internet Explorer by modifying the data value of the Compatibility Flags DWORD within the following location in the registry: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\ActiveX Compatibility\BAAA6516-267C-466D-93F5-C504EF973837 If the Compatibility Flags value is set to 0x00000400, the control can no longer be instantiated inside the browser. For more information, please see: http://support.microsoft.com/kb/240797

## Disclosure Timeline

- 2014-02-10 - Vulnerability reported to vendor
- 2015-02-27 - Coordinated public release of advisory
